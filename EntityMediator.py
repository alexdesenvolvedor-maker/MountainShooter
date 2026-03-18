from Enemy import Enemy
from Entity import Entity


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            EntityMediator.__verify_collision_window(ent)

        # chama o método privado corretamente
        EntityMediator.__verify_health(entity_list)

    @staticmethod
    def __verify_health(entity_list: list[Entity]):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]