package uk.bensonj.adventofcode.day8;

import java.util.List;

public class Day8 {
    private final List<Display> displays;

    public Day8(List<String> data) {
        this.displays = data.stream().map(Display::new).toList();
    }

    public int part1() {
        return displays.stream()
                .mapToInt(d -> d.decode().stream().filter(i -> i > -1).toList().size())
                .sum();
    }

    public int part2() {
        return 0;
    }
}
