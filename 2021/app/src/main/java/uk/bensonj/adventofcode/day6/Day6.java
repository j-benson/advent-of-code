package uk.bensonj.adventofcode.day6;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day6 {
    private Fishiverse fishiverse;
    private static final int RESET = 6;
    private static final int NEW_FISH = 6;

    public Day6(String data) {
        fishiverse = new Fishiverse(Stream.of(data.split(","))
                .mapToInt(Integer::parseInt).toArray());
    }

    public int part1() {
        IntStream.range(0, 80).forEach(i -> fishiverse.goForthOneDay());
        return fishiverse.size();
    }

    public int part2() {
        return 0;
    }
}
