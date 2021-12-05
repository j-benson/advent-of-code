package uk.bensonj.adventofcode;

public class TestPuzzle extends Puzzle {
    @Override
    public String fetchInput(int day) {
        try {
            return new String(getClass()
                    .getResourceAsStream("/day%d.txt".formatted(day))
                    .readAllBytes());
        } catch (Exception e) {
            throw new NopeException(e);
        }
    }
}
