package uk.bensonj.adventofcode;

import kong.unirest.Unirest;

import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;

public class Puzzle {
    public List<String> fetchInputAsLines(int day) {
        return List.of(fetchInput(day).split("\n"));
    }

    public String fetchInput(int day) {
        try {
            var session = new String(Files.readAllBytes(Path.of(".session")));
            var res = Unirest.get("https://adventofcode.com/2021/day/%d/input".formatted(day))
                    .header("Cookie", "session=%s;".formatted(session))
                    .asString();
            return res.getBody();
        } catch (Exception e) {
            throw new NopeException(e);
        }
    }
}
