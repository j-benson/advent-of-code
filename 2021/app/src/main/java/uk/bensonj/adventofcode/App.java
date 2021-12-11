package uk.bensonj.adventofcode;

import uk.bensonj.adventofcode.day8.Day8;

public class App {
    public static void main(String[] args) {
        var puzzle = new Puzzle();
        var app = new App(puzzle);
        app.solve(8, 1);
    }
    private final Puzzle puzzle;
    public App(Puzzle puzzle) {
        this.puzzle = puzzle;
    }

    public void solve(int day, int part) {
        try {
            var answer = new Day8(puzzle.fetchInputAsLines(day)).part1();
            System.out.println(answer);
            System.out.println(puzzle.submit(day, part, answer));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
