package uk.bensonj.adventofcode.day3;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day3Part1Test {
    private Day3Part1 day3Part1;

    @BeforeEach
    void setUp() {
        day3Part1 = new Day3Part1();
    }

    @Test
    void solve() {
        var result = day3Part1.solve(List.of(
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010"
        ));
        assertEquals(198, result);
    }
}
