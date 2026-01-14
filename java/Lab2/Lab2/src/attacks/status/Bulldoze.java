package attacks.status;
import ru.ifmo.se.pokemon.*;

public class Bulldoze extends StatusMove {  // 或者 SpecialMove/PhysicalMove
    // 根据技能类型选择：StatusMove（变化技能）或 SpecialMove/PhysicalMove（攻击技能）

    public Bulldoze() {
        // 参数说明：
        // Type.NORMAL - 技能属性（根据实际技能调整，如 ICE, ROCK 等）
        // 0.0 - 威力（如果是StatusMove就写0.0）
        // 100.0 - 命中率
        super(Type.NORMAL, 0.0, 100.0);
    }

    @Override
    protected void applyOppEffects(Pokemon pokemon) {
        // 100%几率降低对手速度1级
        pokemon.setMod(Stat.SPEED, -1);

        // 可选：添加反馈信息
        System.out.println(pokemon + "的速度降低了！");
    }

    @Override
    protected String describe() {
        return "Used Bulldoze";
    }
}