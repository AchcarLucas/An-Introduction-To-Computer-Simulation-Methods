package src;

public class FallingBallApp {
    public static void main(String[] args) {
        Particle ball = new FallingBall(10, 0);

        ball.t = 0;
        ball.dt = 0.01;

        while (ball.y > 0) {
            ball.step();
        }

        System.out.println("results");
        System.out.println("final time: " + ball.t);
        System.out.println("Simulated");
        System.out.println("y: " + ball.y + " v: " + ball.v);
        System.out.println("Analyzed");
        System.out.println("y: " + ball.analyticPosition() + " v: " + ball.analyticVelocity());

    }
}