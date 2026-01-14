package pokemons;

import attacks.physical.AquaTail;
import attacks.physical.TakeDown;
import attacks.special.IceBeam;
import attacks.status.ScaryFace;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

public class Basculin extends Pokemon {
    public Basculin(String name, int lvl) {
        super(name, lvl);
        setStats(70.0, 92.0, 65.0, 80.0, 55.0, 98.0);
        setType(Type.WATER);
        addMove(new IceBeam());
        addMove(new AquaTail());
        addMove(new ScaryFace());
        addMove(new TakeDown());
    }
}
