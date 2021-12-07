package uk.bensonj.adventofcode.day5;

import java.util.List;

public class Day5 {
    private final List<String> input;

    public Day5(List<String> input) {
        this.input = input;
    }

    public int part1() {
        var hydro = new Hydrothermal(input);
        hydro.excludeDiagonals();
        return hydro.dangerZones();
    }

    public int part2() {
        var hydro = new Hydrothermal(input);
        return hydro.dangerZones();
    }
}
