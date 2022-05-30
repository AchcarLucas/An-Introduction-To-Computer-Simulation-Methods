package src;

// SHO = Spring Harmonic Oscillator
public class SHO extends Particle {
    final static double k = 1.0f;
    // initial position and velocity
    private double x0 = 0;
    private double v0 = 0;
    
    // Omega
    double w = Math.sqrt(k);

    public SHO(double x0, double v0) {
        System.out.println("A new harmonic oscillator object is created.");
        this.x = this.x0 = x0;
        this.v = this.v0 = v0;
    }

    public void step() {
        v = v - k * x * dt;
        x = x + v * dt;
        t = t + dt;
    }

    public double analyticPosition() {
        return x0 * Math.cos(w * t) + (v0 / w) * Math.sin(w * t);
    }

    public double analyticVelocity() {
        return -1 * x0 * w * Math.sin(w * t) + v0 * Math.cos(w * t);
    }
}
