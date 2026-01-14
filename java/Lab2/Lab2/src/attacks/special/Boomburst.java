package attacks.special;

import ru.ifmo.se.pokemon.SpecialMove;
import ru.ifmo.se.pokemon.Type;

public class Boomburst extends SpecialMove {
    public Boomburst() {
        super(Type.NORMAL, 140, 100.0);
    }
    @Override
    protected String describe() {
        return "Used Boomburst";
    }
}
