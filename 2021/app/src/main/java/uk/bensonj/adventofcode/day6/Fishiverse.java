package uk.bensonj.adventofcode.day6;

public class Fishiverse {
    private static final int RESET = 6;
    private static final int NEW_FISH = 8;

    private final int[] fish = new int[Integer.MAX_VALUE / 32];
    private int size = 0;
    private int days = 0;

    public Fishiverse(int[] initialFish) {
        for (var f : initialFish) {
            addFish(f);
        }
    }

    public int days() {
        return days;
    }

    public int size() {
        return size;
    }

    public void addFish(int value) {
        fish[size++] = value;
    }

    public void goForthOneDay() {
        days++;
        var end = size;
        for (int i = 0; i < end; i++) {
            if (fish[i] == 0) {
                fish[i] = RESET;
                addFish(NEW_FISH);
            } else {
                fish[i] = fish[i] - 1;
            }
        }
    }
}
