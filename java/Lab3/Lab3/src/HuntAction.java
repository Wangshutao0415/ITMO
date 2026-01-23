import Animal.Animal;

public class HuntAction {

    public void execute(Player player, Animal animal, Terrain terrain) {
        player.consumeGunpowder(animal.getGunpowderCost());
        player.addMeat(animal.getMeatValue());
        terrain.removeAnimal(animal);
    }
}
