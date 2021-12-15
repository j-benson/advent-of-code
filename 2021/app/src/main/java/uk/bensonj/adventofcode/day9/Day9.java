package uk.bensonj.adventofcode.day9;

import java.util.stream.IntStream;

public class Day9 {
    private HeightMap heightMap;

    public Day9(String data) {
        heightMap = new HeightMap(data);
    }

    public int part1() {
        return IntStream.range(0, heightMap.size())
                .map(i -> heightMap.isLow(i) ? heightMap.value(i) : -1)
                .map(i -> i + 1)
                .sum();
    }
    public int part2() {
        return 0;
    }
}
