package uk.bensonj.adventofcode;

import kong.unirest.Unirest;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.regex.Pattern;

public class Puzzle {

    private String session;

    public Puzzle() {
        Unirest.config().proxy("localhost", 9999);
        try {
            session = new String(Files.readAllBytes(Path.of(".session")));
        } catch (Exception e) {
            session = "";
        }
    }

    public List<String> fetchInputAsLines(int day) {
        return List.of(fetchInput(day).split("\n"));
    }

    public String fetchInput(int day) {
        try {
            var res = Unirest.get("https://adventofcode.com/2021/day/%d/input".formatted(day))
                    .header("Cookie", "session=%s;".formatted(session))
                    .asString();
            return res.getBody();
        } catch (Exception e) {
            throw new NopeException(e);
        }
    }

    public String submit(int day, int part, int answer) {
        var res = Unirest.post("https://adventofcode.com/2021/day/%d/answer".formatted(day))
                .header("Cookie", "session=%s;".formatted(session))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .body("level=%s&answer=%s".formatted(String.valueOf(part), String.valueOf(answer)))
                .asString();

        try {
            if (res.getStatus() != 200) {
                throw new NopeException("Error on submit: %s".formatted(res.getStatus()));
            }

            var ans = new Answer(res.getBody());
            if (ans.correct) {
                return "⭐️";
            } else {
                return "❌️";
            }
        } finally {
            try {
                Files.writeString(Path.of("DEBUG.html"), res.getBody());
            } catch (Exception e) {
                throw new NopeException(e);
            }
        }
    }
}

class Answer {
    private static final Pattern YAY_PATTERN = Pattern.compile("That's the right answer!");
    private static final Pattern SLOW_DOWN_BOI_PATTERN = Pattern.compile("You gave an answer too recently");
    private static final Pattern WAIT_TIME_PATTERN = Pattern.compile("You have [0-9a-z ]* left to wait\\.?");

    public final boolean correct;

    public Answer(String data) {
        var yay = YAY_PATTERN.matcher(data);
        if (yay.matches()) {
            correct = true;
        } else {
            correct = false;
        }

        var wait = SLOW_DOWN_BOI_PATTERN.matcher(data);
        if (wait.matches()) {
            var waitTime = WAIT_TIME_PATTERN.matcher(data);
            throw new NopeException("⏳ %s\n%s".formatted(wait.group(0), waitTime.group(0)));
        }
    }
}
