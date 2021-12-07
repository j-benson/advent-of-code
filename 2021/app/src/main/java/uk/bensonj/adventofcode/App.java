package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day5.Day5;

public class App {
    public static void main(String[] args) {
        try {
            var puzzle = new Puzzle();
            var answer = new Day5(puzzle.fetchInputAsLines(5)).part1();
            System.out.println(answer);
            System.out.println(puzzle.submit(5, 1, answer));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
