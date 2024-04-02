from fields.field import Field

class RecordInfo:
    def __init__(self, tag=None, note=None, notes=None):
        self.tag = Field(tag)
        self.note = Field(note)
        self.notes = notes if notes else {}

    def add_note(self, tag, note):
        self.notes[Field(tag)] = Field(note)

    def edit_note(self, tag, new_note):
        if tag in self.notes:
            self.notes[tag].set_value(new_note)
        else:
            print("Note with this tag does not exist.")

    def remove_note(self, tag):
        if tag in self.notes:
            del self.notes[tag]
            print(f"Success:  note with tag {tag} has been removed successfully. \n")
        else:
            print(f"Note with tag {tag} does not exist.")