
import cliff.command


class Command(cliff.command.Command):
    """Send a command to the linear_acc emulator"""

    def get_parser(self, prog_name):
        ap = super().get_parser(prog_name)
        ap.add_argument('avm_id', help='AVM identifier')
        ap.add_argument('x', type=float, help='linear_acc vector: x (float)')
        ap.add_argument('y', type=float, help='linear_acc vector: y (float)')
        ap.add_argument('z', type=float, help='linear_acc vector: z (float)')
        return ap

    def take_action(self, parsed_args):
        avm_id = parsed_args.avm_id

        payload = {
            'x': parsed_args.x,
            'y': parsed_args.y,
            'z': parsed_args.z,
        }

        self.app.do_post('android', 'sensors', 'linear_acc', avm_id,
                         json=payload)
