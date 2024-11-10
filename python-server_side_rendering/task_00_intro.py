import os

def generate_invitations(template, attendees):

    if not isinstance(template, str):
        print("Invalid template.")
        return

    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input data for attendees.")
        return

    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    for idx, attendee in enumerate(attendees, start=1):
        invitation_text = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Escribir la invitación en un archivo
        file_name = f"output_{idx}.txt"
        try:
            with open(file_name, "w") as file:
                file.write(invitation_text)
        except IOError as e:
            print(f"Error at {file_name}: {e}")