package uk.bensonj.adventofcode.day1;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class Day1Part2Test {
    private Day1Part2 day1Part2;

    @BeforeEach
    public void setUp() {
        day1Part2 = new Day1Part2();
    }

    @Test
    void solve() {
        var result = day1Part2.solve(List.of(
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

        assertEquals(5, result);
    }

}