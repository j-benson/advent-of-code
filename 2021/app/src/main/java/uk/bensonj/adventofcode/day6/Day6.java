package uk.bensonj.adventofcode.day6;

import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Day6 {
    private Fishiverse fishiverse;

    public Day6(String data) {
        fishiverse = new Fishiverse(Stream.of(data.split(","))
                .mapToInt(Integer::parseInt).toArray());
    }

    public long part1() {
        IntStream.range(0, 80).forEach(i -> fishiverse.goForthOneDay());
        return fishiverse.size();
    }

    public long part2() {
        IntStream.range(0, 256).forEach(i -> fishiverse.goForthOneDay());
        return fishiverse.size();
    }
}
