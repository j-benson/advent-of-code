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
            return res.getBody().trim();
        } catch (Exception e) {
            throw new NopeException(e);
        }
    }

    public String submit(int day, int part, int answer) {
        return submit(day, part, String.valueOf(answer));
    }

    public String submit(int day, int part, long answer) {
        return submit(day, part, String.valueOf(answer));
    }

    public String submit(int day, int part, String answer) {
        var res = Unirest.post("https://adventofcode.com/2021/day/%d/answer".formatted(day))
                .header("Cookie", "session=%s;".formatted(session))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .body("level=%s&answer=%s".formatted(String.valueOf(part), answer))
                .asString();

        try {
            if (res.getStatus() != 200) {
                throw new NopeException("Error on submit: %s".formatted(res.getStatus()));
            }

            var ans = new Answer(res.getBody());
            if (ans.correct) {
                return "⭐️";
            } else if (!ans.message.isEmpty()) {
                return "❌ " + ans.message;
            } else {
                return "❌";
            }
        } finally {
            try {
                Files.writeString(Path.of("DEBUG.html"), res.getBody());
            } catch (Exception ignored) {
            }
        }
    }
}

class Answer {
    public final boolean correct;
    public String message = "";

    public Answer(String data) {
        correct = data.toLowerCase().contains("that's the right answer");
        if (!correct) {
            var reason = Pattern.compile("your answer is[\\w\\s]+",
                    Pattern.DOTALL & Pattern.CASE_INSENSITIVE).matcher(data);
            if (reason.find()) {
                message = reason.group(0);
            }
            var wait = Pattern.compile("you gave an answer too recently",
                    Pattern.DOTALL & Pattern.CASE_INSENSITIVE).matcher(data);
            if (wait.find()) {
                var waitTime = Pattern.compile("you have [\\d\\w\\s]* left to wait",
                        Pattern.DOTALL & Pattern.CASE_INSENSITIVE).matcher(data);
                waitTime.find();
                message = "⏳ %s\n%s".formatted(wait.group(0), waitTime.group(0));
            }
        }
    }
}
