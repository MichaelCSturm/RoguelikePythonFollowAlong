from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.KeySym(1073741906):
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.KeySym(1073741905):
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.KeySym(1073741904):
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.KeySym(1073741903):
            action = MovementAction(dx=1, dy=0)

        elif key == tcod.event.KeySym.ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action