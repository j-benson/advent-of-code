package uk.bensonj.adventofcode.day4;

public class Day4 {
    public int part1(String input) {
        var bingo = new Bingo(input);
        var lastNumber = -1;
        while (!bingo.hasWinner()) {
            lastNumber = bingo.callAndMark();
        }
        var winner = bingo.getWinner();
        return winner.unmarkedNumbersSum() * lastNumber;
    }

    public int part2(String input) {
        var bingo = new Bingo(input);
        var lastNumber = -1;
        while (bingo.hasPlayers()) {
            lastNumber = bingo.callAndMark();
        }
        var lastWinner = bingo.getLastWinner();
        return lastWinner.unmarkedNumbersSum() * lastNumber;
    }
}
