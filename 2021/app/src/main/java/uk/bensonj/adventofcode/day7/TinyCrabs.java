package uk.bensonj.adventofcode.day7;

import uk.bensonj.adventofcode.modules.MathUtils;

import java.util.*;
import java.util.stream.IntStream;

public class TinyCrabs {
    private final List<Integer> xPositions;
    private final int minX;
    private final int maxX;
    private boolean advancedFuelCost = false;
    private int fuel = 0;

    public TinyCrabs(List<Integer> xPositions) {
        this.xPositions = xPositions;
        minX = xPositions.stream().min(Integer::compareTo).orElse(0);
        maxX = xPositions.stream().max(Integer::compareTo).orElse(0);
    }

    public void assemble(boolean useAdvancedFuelCost) {
        advancedFuelCost = useAdvancedFuelCost;
        fuel = IntStream.rangeClosed(minX, maxX).map(x ->
                xPositions.stream()
                        .mapToInt(xx -> Math.max(x, xx) - Math.min(x, xx))
                        .map(this::fuelCost).sum()
        ).min().orElseThrow();
    }
    private int fuelCost(int movement) {
        if (advancedFuelCost){
            return MathUtils.triangular(movement);
        }
        return movement;
    }

    public int fuel() {
        return fuel;
    }
}
