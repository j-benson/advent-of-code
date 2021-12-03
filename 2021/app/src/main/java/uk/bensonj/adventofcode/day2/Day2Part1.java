package uk.bensonj.adventofcode.day2;

import java.util.List;

public class Day2Part1 {
    public static class Sub {
        private int depth, horizontal;

        public void forward(String value) {
            horizontal += Integer.parseInt(value);
        }

        public void up(String value) {
            depth -= Integer.parseInt(value);
        }

        public void down(String value) {
            depth += Integer.parseInt(value);
        }

        public int position() {
            return depth * horizontal;
        }
    }

    public int solve(List<String> input) {
        var sub = new Day2Part1.Sub();
        var pairs = input.stream().map(i -> i.split(" ")).toList();
        pairs.forEach(p -> {
            switch (p[0]) {
                case "forward" -> sub.forward(p[1]);
                case "up" -> sub.up(p[1]);
                case "down" -> sub.down(p[1]);
            }
        });
        return sub.position();
    }
}
