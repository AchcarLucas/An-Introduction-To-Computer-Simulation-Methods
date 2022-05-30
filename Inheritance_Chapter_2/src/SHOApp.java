package src;

public class SHOApp {
    public static void main(String[] args) {
        Particle spring = new SHO(1, 0);

        spring.t = 0;
        spring.dt = 0.01;

        int N = 0;

        while (N <= 1000) {
            spring.step();
            ++N;
        }

        System.out.println("results");
        System.out.println("final time: " + spring.t);
        System.out.println("Simulated");
        System.out.println("x: " + spring.x + " v: " + spring.v);
        System.out.println("Analyzed");
        System.out.println("x: " + spring.analyticPosition() + " v: " + spring.analyticVelocity());
    }
}
