package uk.bensonj.adventofcode.day2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day2Part2Test {
    private Day2Part2 day2Part2;

    @BeforeEach public void setUp() {
        day2Part2 = new Day2Part2();
    }

    @Test public void solve() {
        var result = day2Part2.solve(List.of(
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"
        ));
        assertEquals(900, result);
    }
}