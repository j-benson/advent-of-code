package uk.bensonj.adventofcode.day2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day2Part1Test {
    private Day2Part1 day2Part1;

    @BeforeEach
    public void setUp() {
        day2Part1 = new Day2Part1();
    }

    @Test
    public void solve() {
        var result = day2Part1.solve(List.of(
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2"
        ));

        assertEquals(150, result);
    }
}