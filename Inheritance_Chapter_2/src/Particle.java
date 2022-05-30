package src;

abstract public class Particle {
    double x, y, v, t;
    double dt;

    public Particle() {
        System.out.println("A new Particle is created");
    }

    abstract protected void step();
    abstract protected double analyticPosition();
    abstract protected double analyticVelocity();
}
