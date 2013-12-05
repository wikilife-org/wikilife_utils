# coding=utf-8

from wikilife_utils.google_visualization import hlg_gviz_api as gviz_api


class DataFormatter():

    def __init__(self, description, data, custom_values):
        self.description = description
        self.data = data
        self.custom_values = custom_values

    def google_visualization(self):
        # Loading it into gviz_api.DataTable
        data_table = gviz_api.DataTable(self.description, custom_properties=self.custom_values)
        data_table.LoadData(self.data)

        # Creating a JSon string
        json = data_table.ToJSon()
        return json

    def to_xml(self):
        if self.custom_values["row_name"]:
            row_name = self.custom_values["row_name"]
        fields = []
        for key in self.description.keys():
            fields.append(key)
        xml = '<?xml version="1.0" encoding="UTF-8"?> <root>'
        if "init" in self.custom_values:
            xml += '<%s>' % self.custom_values["init"]
        if len(self.data) > 0:
            for i in self.data:
                xml += ' <%s> ' % row_name
                for field in fields:
                    field_name = self.custom_values[field]
                    xml += '<{}>{}</{}> '.format(field_name, i[field], field_name)
                if len(fields) == 1:
                    xml += ' <text>'
                    xml += self.description.values()[0][1]
                    xml += '</text>'
                xml += ' </%s> ' % row_name
        else:
            xml += 'NO DATA'
        if "init" in self.custom_values:
            xml += '</%s>' % self.custom_values["init"]
        xml += '</root>'
        return xml

    def to_json(self):
        table = {}
        table["cols"] = []
        table["rows"] = []
        table["title"] = self.custom_values["stats_name"]

        del self.custom_values["stats_name"]

        desc_keys = self.description.keys()

        for desc_key in desc_keys:
            desc_obj = self.description[desc_key]
            table["cols"].append({"type": desc_obj[0], "label": desc_obj[1]})

        for table_data in self.data:
            row = []
            for desc_key in desc_keys:
                row.append(table_data[desc_key])
            table["rows"].append(row)

        result = {}
        result["table"] = table
        result.update(self.custom_values)

        return result
