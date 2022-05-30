package src;

public class FallingBall extends Particle {
    final static double g = 9.8f;
    // initial position and velocity
    private double y0 = 0;
    private double v0 = 0;

    public FallingBall(double y0, double v0) {
        System.out.println("A new Falling Particle object is created");
        this.y = this.y0 = y0;
        this.v = this.v0 = v0;
    }

    public void step() {
        y = y + v * dt;
        v = v - g * dt;
        t = t + dt;
    }

    public double analyticPosition() {
        return y0 + v0 * t - (g * t * t) / 2.0;
    }

    public double analyticVelocity() {
        return v0 - g * t;
    }
}
