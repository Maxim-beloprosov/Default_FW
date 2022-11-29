from fw.g1_api.users.g1_api_users import G1ApiUsers


class G1ApiUsersWrapper(G1ApiUsers):

    def get_user_id_region(self, name_region):
        response = self.manager.g1_api_users.get_users_regions()
        for region in response:
            if region['Name'] == name_region:
                return region['Id']
