package uk.bensonj.adventofcode.day8;

import java.util.List;

public class Display {
    private final List<String> signal;
    private final List<String> output;

    public Display(String data) {
        var d = List.of(data.split(" "));
        var i = d.indexOf("|");
        signal = d.subList(0, i);
        output = d.subList(i+1, d.size());
    }

    public List<Integer> decode() {
        return output.stream().mapToInt(this::decodeDigit).boxed().toList();
    }
    private int decodeDigit(String input) {
        return switch (input.length()) {
            case 2 -> 1;
            case 3 -> 7;
            case 4 -> 4;
            case 7 -> 8;
            default -> -1;
        };
    }
}
