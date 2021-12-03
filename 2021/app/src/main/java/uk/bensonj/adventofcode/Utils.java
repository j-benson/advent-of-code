package uk.bensonj.adventofcode;

import kong.unirest.Unirest;

import java.util.Arrays;
import java.util.List;

public class Utils {
    public List<String> fetchPuzzleInputAsLines(Integer day) {
        return Arrays.asList(fetchPuzzleInput(day).split("\n"));
    }

    public String fetchPuzzleInput(Integer day) {
        Unirest.config().proxy("localhost", 9999);
        var res = Unirest.get("https://adventofcode.com/2021/day/%d/input".formatted(day))
                .header("Cookie", "session=%s;".formatted("53616c7465645f5f76e449fda7b8382a563b8a2839fa21a84329e94bcff9ed6a675fe071a9c6509413b4229b4c40a686"))
                .header("Connection", "Keep-Alive")
                .asString();
        return res.getBody();
    }
}
