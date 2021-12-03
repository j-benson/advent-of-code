package uk.bensonj.adventofcode.day1;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day1Part1Test {
    private Day1Part1 day1Part1;

    @BeforeEach
    public void setUp() {
        day1Part1 = new Day1Part1();
    }

    @Test
    void solve() {
        var result = day1Part1.solve(List.of(
                "199",
                "200",
                "208",
                "210",
                "200",
                "207",
                "240",
                "269",
                "260",
                "263"
        ));

        assertEquals(7, result);
    }
}
