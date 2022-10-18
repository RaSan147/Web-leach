from main_ez import main, ProjectType_

main.make_required_dirs()
main.get_user()
# main.main_loop()

class AppHandler:
    def __init__(self):
        self.ids = dict() # contains the pointers of the main_loop # actually not loops but threads
        
    def new_process(self, PID):
        self.ids[PID] = ProjectType_()

    def kill_process(self, PID):
        success = self.ids[PID].kill()
        del self.ids[PID]

        return success

    def send_json(self, PID, json, data_type):
        """
        Push Json to the Project for processing
        PID: SERVER Handler ID
        json: JSON data
        data_type: Data type (projdat | projlist)"""
        output = self.ids[PID].send_json(json, data_type)

        return output

    def get_json(self, PID, data_type):
        """
        Get JSON data from the Project for processing
        PID: SERVER Handler ID
        data_type: Data type (projdat | projlist)
        """
        output = self.ids[PID].get_json(data_type)

        return output

    def save_state(self, PID):
        """
        Save the state of the Project
        PID: SERVER Handler ID
        """
        self.ids[PID].store_current_data()

    def start_download(self, PID, thread_count=10):
        """
        Start the download of the Project
        PID: SERVER Handler ID
        thread_count: Number of threads
        """
        self.ids[PID].start_download(thread_count)

    def start_link_index(self, PID, thread_count=3):
        """
        Start the link index of the Project
        PID: SERVER Handler ID
        thread_count: Number of threads
        """
        self.ids[PID].start_link_index(thread_count)

    
# h = AppHandler()
# h.send_json()

class HandleRequests:
    def __init__(self):
        pass

    def handle_request(self, PID, request):


        pass