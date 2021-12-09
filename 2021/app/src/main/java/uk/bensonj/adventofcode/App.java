package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day7.Day7;

public class App {
    public static void main(String[] args) {
        try {
            var puzzle = new Puzzle();
            var answer = new Day7(puzzle.fetchInput(7)).part1();
            System.out.println(answer);
            System.out.println(puzzle.submit(7, 1, answer));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
