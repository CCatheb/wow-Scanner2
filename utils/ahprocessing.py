import numpy as np

class DataProcessing:

    item_id = None

    def get_auctions_by_id(self, auctions):
        """ Filters a list of auctions using the item ID.

            Parameters
            ----------
            auctions (list)
                List of all the auctions. Each auction has to be presented in a
            dict.

            Returns
            -------
            auctions_id_list
                List of all the auctions matching the item ID.
        """
        j=0
        auctions_id_list = []
        dict = {
            "quantity" : 0,
            "unit_price" : 0
            }

        for i in range(len(auctions)):
            if auctions[i]["item"]["id"] == self.item_id:
                dict["quantity"] = auctions[i]["quantity"]
                dict["unit_price"] = int(auctions[i]["unit_price"]/10000)
                # We have to add copy otherwise we just add references to the list
                auctions_id_list.append(dict.copy())
                j += 1

        print("Number of auctions for item n. "+ str(self.item_id) + " : " + str(j))
        return auctions_id_list


    def process_data(self, auctions_id_list, sensibility=5):
        """ Creates usable data (e.g number of auctions, number of items currently
        in sell, average value, etc) for humans.

            Parameters
            ----------
            auctions_id_list (list)
                List of all the auctions regarding ONE item
            sensibility (int)
                Filtering sensibility for the median value. Lower it is, harder
                will be the filter. Filter based on removing any price over
                (sesibility * median) value

            Returns
            -------
            quantity (int)
                Quantity of items currently with auctions
            average_value (int)
                Average seeling value regarding the current auctions
            min_value (int)
                Minimal price for the item
        """

        quantity = 0
        total_amount = 0
        average_value = 0
        quantity_list = []
        amount_list = []

        for i in range(len(auctions_id_list)):
            quantity = quantity + auctions_id_list[i]["quantity"]
            total_amount = total_amount + auctions_id_list[i]["unit_price"]
            quantity_list.append(auctions_id_list[i]["quantity"])
            amount_list.append(auctions_id_list[i]["unit_price"])
        if quantity != 0:
            average_value = np.median(np.array(amount_list))
            min_value = min(amount_list)

            for value in amount_list:
                if value > (sensibility*average_value):
                    amount_list.remove(value)

        return (quantity, int(average_value), int(min_value))
