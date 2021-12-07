package uk.bensonj.adventofcode;

public class NopeException extends RuntimeException {
    public NopeException() {
        super();
    }
    public NopeException(String message) {
        super(message);
    }
    public NopeException(Throwable cause) {
        super(cause);
    }
}
