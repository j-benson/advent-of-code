package uk.bensonj.adventofcode.day3;

import java.util.List;

public class Day3Part2 {
    public int solve(List<String> input) {
        var diagnostics = new Diagnostic(input);
        return diagnostics.oxygenGeneratorRating() * diagnostics.co2ScrubberRating();
    }
}
