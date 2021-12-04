package uk.bensonj.adventofcode.day3;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day3Part2Test {

    private Day3Part2 day3Part2;

    @BeforeEach
    void setUp() {
        day3Part2 = new Day3Part2();
    }

    @Test
    void solve() {
        var result = day3Part2.solve(List.of(
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
        assertEquals(23, result);
        assertEquals(230, result);
    }
}