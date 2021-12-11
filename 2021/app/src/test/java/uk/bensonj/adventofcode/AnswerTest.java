package uk.bensonj.adventofcode;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AnswerTest {
    private String load(String name) {
        try {
            return new String(getClass().getResourceAsStream("/answers/%s.html".formatted(name)).readAllBytes());
        } catch (Exception e) {
            return "";
        }
    }

    @Test
    public void success() {
        var answer = new Answer(load("right"));
        assertTrue(answer.correct);
    }

    @Test
    public void fail() {
        var answer = new Answer(load("not-right"));
        assertFalse(answer.correct);
        assertEquals("your answer is too low", answer.message);
    }

    @Test
    public void tooRecent() {
        var answer = new Answer(load("too-recent"));
        assertFalse(answer.correct);
        assertEquals("You gave an answer too recently\nYou have 30 seconds left to wait", answer.message);
    }
}
