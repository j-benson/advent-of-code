package uk.bensonj.adventofcode.day1;

import java.util.List;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;

public class Part1 {
    public Integer solve(List<String> input) {
        var values = input.stream().mapToInt(Integer::parseInt).boxed().collect(toList());
        return IntStream.range(1, input.size()).map(i -> values.get(i) > values.get(i-1) ? 1 : 0).sum();
    }
}
