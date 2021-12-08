package uk.bensonj.adventofcode.day6;

public class Fishiverse {
    private static final int NEW_FISH = 8;
    private static final int PARENT_FISH = 6;
    private static final int PREGGERS_FISH = 0;
    private final long[] fish = new long[NEW_FISH + 1];
    private int fishDealer = PREGGERS_FISH;

    public Fishiverse(int[] initialFish) {
        for (var f : initialFish) {
            addFish(f);
        }
    }

    public long size() {
        long size = 0;
        for (long f : fish) {
            size += f;
        }
        return size;
    }

    public void addFish(int age) {
        addFish(age, 1);
    }
    public void addFish(int age, long numberOfFish) {
        fish[position(age)] += numberOfFish;
    }
    public long getFish(int age) {
        return fish[position(age)];
    }
    public void removeFish(int age) {
        fish[position(age)] = 0;
    }
    private int position(int value) {
        return (value + fishDealer) % (NEW_FISH + 1);
    }
    private void moveFishDealerOn() {
        fishDealer += 1;
    }

    public void goForthOneDay() {
        var preggers = getFish(PREGGERS_FISH);
        removeFish(PREGGERS_FISH);
        moveFishDealerOn();
        addFish(PARENT_FISH, preggers);
        addFish(NEW_FISH, preggers);
    }
}
