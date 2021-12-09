package uk.bensonj.adventofcode.day7;

import java.util.*;

public class TinyCrabs {
    private final List<Integer> xPositions;
    private int fuel = 0;

    public TinyCrabs(List<Integer> xPositions) {
        this.xPositions = xPositions;
    }

    public void assemble() {
        fuel = xPositions.stream().mapToInt(x ->
                xPositions.stream().mapToInt(xx -> Math.max(x, xx) - Math.min(x, xx)).sum()
        ).min().orElseThrow();
    }

    public int fuel() {
        return fuel;
    }
}
