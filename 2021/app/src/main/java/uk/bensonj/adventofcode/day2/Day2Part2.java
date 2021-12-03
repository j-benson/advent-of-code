package uk.bensonj.adventofcode.day2;

import java.util.List;

public class Day2Part2 {
    public static class Sub {
        private int depth, horizontal, aim;

        public void forward(String value) {
            var x = Integer.parseInt(value);
            horizontal += x;
            depth += aim * x;
        }

        public void up(String value) {
            aim -= Integer.parseInt(value);
        }

        public void down(String value) {
            aim += Integer.parseInt(value);
        }

        public int position() {
            return depth * horizontal;
        }
    }

    public int solve(List<String> input) {
        var sub = new Day2Part2.Sub();
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
