import Animal.Bird;
import Animal.Turtle;

public class Beach extends Terrain {

    @Override
    protected void spawnAnimals() {
        int birds = random.nextInt(2) + 2;
        int turtles = random.nextInt(2) + 2;

        for (int i = 0; i < birds; i++) {
            animals.add(new Bird());
        }
        for (int i = 0; i < turtles; i++) {
            animals.add(new Turtle());
        }
    }
}
