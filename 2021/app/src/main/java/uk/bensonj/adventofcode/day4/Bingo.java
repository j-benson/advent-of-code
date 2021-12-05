package uk.bensonj.adventofcode.day4;

import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Bingo {
    private final BingoHost bingoHost;
    private final List<BingoBoard> bingoBoards;
    private BingoBoard winner;

    public Bingo(String data) {
        var elements = data.split("\n\n");
        bingoHost = new BingoHost(elements[0]);
        bingoBoards = IntStream.range(1, elements.length).mapToObj(i -> new BingoBoard(elements[i])).toList();
    }
    public int callAndMark() {
        var number = bingoHost.callNextNumber();
        bingoBoards.forEach(b -> b.mark(number));
        var hasWinner = bingoBoards.stream().filter(BingoBoard::hasWon).findFirst();
        hasWinner.ifPresent(w -> winner = w);
        return number;
    }
    public boolean hasWinner() {
        return winner != null;
    }
    public BingoBoard getWinner() {
        return winner;
    }

    @Override
    public String toString() {
        var s = new StringBuilder();
        bingoBoards.forEach(b -> s.append(b.toString()).append("\n\n"));
        return s.toString();
    }
}

class BingoHost {
    private final ArrayDeque<Integer> numbers;

    public BingoHost(String data) {
        numbers = new ArrayDeque<>(
                Stream.of(data.split(","))
                    .mapToInt(Integer::parseInt)
                    .boxed()
                    .toList()
        );
    }

    public int callNextNumber() {
        return numbers.removeFirst();
    }
}

class BingoBoard {
    private static final int CAPACITY = 5*5;
    private final List<List<Number>> rows;
    private final List<List<Number>> columns;
    private final Map<Integer, Number> numbers = new HashMap<>(CAPACITY);

    public class Number {
        public final Integer value;
        private Boolean marked = false;

        public Number(String data) {
            value = Integer.parseInt(data);
            numbers.put(value, this);
        }
        public int value() {
            return value;
        }
        public void mark() {
            marked = true;
        }
        public Boolean isMarked() {
            return marked;
        }
        public Boolean isNotMarked() {
            return !marked;
        }

        @Override
        public String toString() {
            return "Number(value=%d, marked=%b)".formatted(value, marked);
        }
    }

    public BingoBoard(String data) {
        rows = Stream.of(data.split("\n"))
                .map(row -> row.split("\s+"))
                .map(row -> Stream.of(row).filter(element -> !"".equals(element))
                        .map(Number::new)
                        .toList()
                ).toList();
        columns = new ArrayList<>(5);
        IntStream.range(0, rows.size()).forEach(i -> {
            var column = new ArrayList<Number>(5);
            IntStream.range(0, rows.get(0).size()).forEach(ii -> {
                column.add(rows.get(ii).get(i));
            });
            columns.add(column);
        });

    }
    public void mark(int number) {
        try {
            numbers.get(number).mark();
        } catch (NullPointerException ignored) { }
    }
    public boolean hasWon() {
        return rows.stream().anyMatch(row -> row.stream().allMatch(Number::isMarked))
                || columns.stream().anyMatch(col -> col.stream().allMatch(Number::isMarked));
    }
    public int unmarkedNumbersSum() {
        return numbers.values().stream().filter(Number::isNotMarked)
                .mapToInt(Number::value)
                .sum();
    }
    @Override
    public String toString() {
        return rows.stream().map(
                row -> row.stream().map(Number::toString).reduce("",(acc, next) -> "".equals(acc) ? next : "%s,%s".formatted(acc, next))
        ).reduce("", (acc, next) -> "".equals(acc) ? next : "%s\n%s".formatted(acc, next));
    }
}
