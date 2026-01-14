package pokemons;
import attacks.status.Moonblast;
import ru.ifmo.se.pokemon.Type;


public class Whimsicott extends Cottonee {
    public Whimsicott(String name, int lvl) {
        super(name, lvl);
        setStats(60.0, 67.0, 85.0, 77.0, 75.0, 116.0);
        setType(Type.GRASS,Type.FAIRY);
        setMove(new Moonblast());
    }
}

