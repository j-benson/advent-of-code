package uk.bensonj.adventofcode.day7;

import java.util.stream.Stream;

public class Day7 {
    private TinyCrabs tinyCrabs;

    public Day7(String input) {
        tinyCrabs = new TinyCrabs(Stream.of(input.split(","))
                .mapToInt(Integer::parseInt).boxed().toList());
    }

    public int part1() {
        tinyCrabs.assemble();
        return tinyCrabs.fuel();
    }

    public int part2() {
        return 0;
    }
}
