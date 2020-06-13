from discord import Member
from typing import Set


class MentorAdapterInterface:
    # Return true if the member is busy.
    def check_busy(self, member: Member) -> bool:
        pass

    # Set member's status.
    def set_busy(self, member: Member, busy: bool) -> None:
        pass


# Implementation of Mentor Adapter Interface Using Pure Python
class OnMemoryMentorAdapter(MentorAdapterInterface):
    def __init__(self):
        self._busy_members: Set[Member] = set()

    def check_busy(self, member: Member) -> bool:
        return member in self._busy_members

    def set_busy(self, member: Member, busy: bool) -> None:
        if busy:
            self._busy_members.add(member)
        else:
            self._busy_members.discard(member)


# Mentor adapter instance.
mentorAdapter: MentorAdapterInterface = OnMemoryMentorAdapter()
