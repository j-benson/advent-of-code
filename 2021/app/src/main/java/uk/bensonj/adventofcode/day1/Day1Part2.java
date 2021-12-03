package uk.bensonj.adventofcode.day1;

import java.util.List;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.toList;

public class Day1Part2 {
    public static class Window {
        private int a, b, c;

        public Window(Integer a, Integer b, Integer c) {
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public int sum() {
            return a + b + c;
        }
    }

    public int solve(List<String> input) {
        var values = input.stream().mapToInt(Integer::parseInt).boxed().collect(toList());
        var windows = IntStream.range(3, input.size())
                .mapToObj(i -> new Window(values.get(i-2), values.get(i-1), values.get(i))).toList();
        return IntStream.range(1, windows.size())
                .map(i -> windows.get(i).sum() > windows.get(i-1).sum() ? 1 : 0).sum() + 1;
    }
}
